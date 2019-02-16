from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

class Block:

    num = 3;
    def __init__(self, data, previousBlock=None):
        self.data = data
        self.__previousBlock = previousBlock
        self.__hash = None if previousBlock==None else previousBlock.computeHash()



    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(bytes(str(self.__data) +  str(self.num), 'utf8'))

        return digest.finalize()

    def getHash(self):
        return self.__hash

    def getPreviousBlock(self):
        return self.__previousBlock

    def getData(self):
        return self.__data

if __name__ == "__main__":

    b = Block( 'b')
    b1 = Block('b1' , b)
    b2 = Block('b2' , b1)
    b3 = Block('b3', b2)

    blocks = [ b1,b2,b3]

    for block in blocks:
        if block.getHash() == block.getPreviousBlock().computeHash():
            print('True')
        else:
            print('Error')
