package sushi_buffer;

import java.io.IOException;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class RunningSushiBuffer<T> {
	private T theBuffer[];
	private Lock lock = new ReentrantLock();
	private Condition zeroVuoto = lock.newCondition();
	private Condition empty = lock.newCondition();
    private Integer indiceZero;
	
	@SuppressWarnings("unchecked")
	public RunningSushiBuffer(final int dim) {
		
		setTheBuffer((T[]) new Object[dim]);
		indiceZero=0;
	}

	public void put(final T c) {
		lock.lock();
		
		while (theBuffer[indiceZero]!=null) {
			try {
				zeroVuoto.await();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		}

		theBuffer[indiceZero] = c;
		
		//in = (in + 1) % theBuffer.length;
		//empty.signalAll();
		lock.unlock();
	}

	public T get(int i) {
		int pos = (i+indiceZero)%theBuffer.length;
		

		if(pos<1 || pos>theBuffer.length) {
			try {
				throw new IOException();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		
		lock.lock();
		try {
			while (theBuffer[pos]==null) {
				try {
					empty.await();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

			}

			T returnValue;

			returnValue = theBuffer[pos];
			theBuffer[pos]=null;

			return returnValue;
		} finally {
			lock.unlock();
		}
	}
	
	
	public void shift(int j) {
		lock.lock();
		
		// uso zeroPosition per spostare la posizione 
		//solo virtualmente, anzichè dover ricopiare degli elementi
				
		
		indiceZero=(indiceZero-j)%theBuffer.length;
		
		//
		//   E' solo grazie a uno shift che può crearsi
		// la condizione per svegliare un thread
		//   in attesa, rispettivamente su put() o su get()
		//
		
		empty.signalAll();
		zeroVuoto.signalAll();
		
		
		
		lock.unlock();
	}
	
	public void shift() {
		shift(1);
	}
	
	

	public T[] getTheBuffer() {
		return theBuffer;
	}

	public void setTheBuffer(T thebuffer[]) {
		this.theBuffer = thebuffer;
	}


	public Lock getLock() {
		return lock;
	}

	public void setLock(Lock lock) {
		this.lock = lock;
	}

	public Condition getFull() {
		return zeroVuoto;
	}

	public void setFull(Condition full) {
		this.zeroVuoto = full;
	}

	public Condition getEmpty() {
		return empty;
	}

	public void setEmpty(Condition empty) {
		this.empty = empty;
	}
}