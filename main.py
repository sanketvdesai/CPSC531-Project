from TrainData import train
from TrainData import analyzeEmail
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from createDatabase import createTables
def main():
    #Create database
    #createTables()
    #Iitiate to 0
    totalSpamWord = 0
    totalHamWord = 0
    totalEmail = 0
    numberOfSpam = 0

    #will not return anything, will just modify current values and
    #modify database
    train(totalSpamWord,totalHamWord,totalEmail,numberOfSpam,0,0,0)







if __name__ == '__main__':
    main()
