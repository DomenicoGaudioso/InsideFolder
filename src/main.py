import pandas as pd
import os

def elenca_files_cartella(path_cartella):
    elenco_files = []
    
    # Scandisci ricorsivamente la cartella e le sue sottocartelle
    for cartella_corrente, sottocartelle, files in os.walk(path_cartella):
        for file in files:
            percorso_file = os.path.join(cartella_corrente, file)
            elenco_files.append(percorso_file)

    return elenco_files

def make_hyperlink(value):
    #url = "https://custom.url/{}"
    nome = value.split("\\")[-1]
    return '=HYPERLINK("%s", "%s")' % (value, nome)

def create_link(url):
    # returns the final component of a path 
    f_url = os.path.basename(url) 
    nome = url.split("\\")[-1]
      
    # convert the path into clickable link 
    return '<a href="{}">{}</a>'.format(url, nome) 

def makeDataframe(listName, listLink):
    d = {"Name": listName, "URL": listLink} 
    df = pd.DataFrame(d)
    # applying function "fun" on column "location". 
    #df = df.style.format({'URL': create_link}) 
    #df['link'] = [create_link(url) for url in df["URL"]]

    return df

def createExcelfromMultipleDataFrame(listDataFrame, listName, path):
    # create a excel writer object as shown using
    # Excelwriter function
    pathExcel = os.path.join(path, "ListOfFileInsedeFolder.xlsx")
    with pd.ExcelWriter(pathExcel, mode="w") as writer:
        for iName, idf in zip(listName, listDataFrame):
            idf['hyperlink'] = idf['URL'].apply(make_hyperlink)
            idf.iloc[:,0] = 'background-color: red'
            idf.to_excel(writer, sheet_name=iName)
            

    return "finish"


def openFolder(pathFolder, type=None):
    # Ottieni la lista di elementi nella cartella (sia cartelle che file)
    elenco_elementi = os.listdir(pathFolder)
    insedeFolder = []
    insedeFile = []
    # Stampa sia cartelle che file in base al parametro 'type'
    for elemento in elenco_elementi:
        percorso_elemento = os.path.join(pathFolder, elemento)
        
        # Verifica se l'elemento è una cartella
        if os.path.isdir(percorso_elemento) and (type is None or type == 'folder'):
            #print(f"Cartella: {elemento}")
            insedeFolder.append(elemento)
        
        # Verifica se l'elemento è un file
        elif os.path.isfile(percorso_elemento) and (type is None or type == 'file'):
            #print(f"File: {elemento}")
            insedeFile.append(elemento)
    
    # Scandisci ricorsivamente le sottocartelle
    dataFrameList = []
    for sottocartella in insedeFolder:
        percorso_sottocartella = os.path.join(pathFolder, sottocartella)
        nomeSottocartella = sottocartella
        percorsoFile = elenca_files_cartella(percorso_sottocartella)
        nomeFile = [ i.split("\\")[-1] for i in percorsoFile]
        #print(nomeFile)
        
        # create dataframe
        dataFrameList.append(makeDataframe(nomeFile, percorsoFile))
    
    return dataFrameList, insedeFolder





# Imposta il percorso della cartella
#pathFolder = r"z:\studio\CODIFICATE\239_S_SS177_Longobucco\documenti iniziali\Ordinati"

#openFolder(pathFolder)