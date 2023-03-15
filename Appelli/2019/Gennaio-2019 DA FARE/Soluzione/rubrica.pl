=begin Traccia esame Gennaio 2019
Si scriva uno script Perl da nome rubrica.pl. Lo script dovrà modellare l'utilizzo e la gestione dei contatti salvati
in rubrica dall'utente. In particolare lo script metterà a disposizione 4 diverse funzionalità, ovvero l'aggiunta,
la rimozione, la ricerca e l'esportazione dei contatti in rubrica.

In particolare lo script dovrà funzionare nel seguente modo:
una volta avviato lo script ("./rubrica.pl" o "perl rubrica.pl") all'utente sarà richiesto di effettuare 1 delle operazioni
messe a disposizione dallo script (aggiunta --> opzione "-a", rimozione --> opzione "-d", ricerca --> opzione "-s"
o esportazione --> opzione "-e") tramite l'immissione da tastiera del parametro opportuno. L'utente effettuerà quindi
l'operazione e lo script continuerà a girare finchè l'utente non deciderà di fermarlo (kill --> opzione -k)

I metodi richiesti sono descritti nel dettaglio di seguito.

N.B. Non sono accettati argomenti iniziali
N.B. Per semplicità si assume che il nome e il cognome dei contatti non contengano il carattere ","
=end Traccia esame Gennaio 2019
=cut

############## Opzione 1 -a ##############
# Aggiunge contatti alla rubrica
# Inserire la stringa "Nome, Cognome, Numero_di_telefono"
# Se il contatto esiste già in rubrica allora aggiornarlo con il nuovo numero di telefono, altrimenti crea una nuova voce
# Il numero di telefono deve essere controllato: non possono essere presenti caratteri o simboli
# e deve essere composto esattamente da 10 cifre



############## Opzione 2 -d ##############
# Rimuove un contatto dalla rubrica
# Inserire la stringa "Nome, Cognome"
# il contatto dovrà essere cancellato dalla rubrica (ammesso che esista)



############## Opzione 3 -s ##############
# Ricerca un contatto in rubrica
# Inserire la stringa "Nome" o "Nome, Cognome"
# e mostrare in ouput tutti i contatti corrispondenti nel formato:
# Nome, Cognome, Numero_di_telefono



############## Opzione 4 -e ##############
# Esporta la lista dei contatti su un file dal nome "contatti.vcf" ordinati alfabeticamente
# Il formato del file dovrà essere il seguente
# BEGIN:VCARD
# VERSION:2.1
# FN:Nome Cognome
# N:Cognome;Nome;;;
# TEL;CELL: Numero_di_telefono 
# END:VCARD



############## Opzione 5 -k ##############
# Termina lo script