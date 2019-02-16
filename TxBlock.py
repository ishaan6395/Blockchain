from Block import Block
from Signatures import generate_keys, sign, verify
from keytest import TX
import pickle

class TxBlock(Block):


    def __init__(self, previousBlock=None):
        super(TxBlock, self).__init__([], previousBlock)

    def addTx(self, tx_in):
        self.data = tx_in

    def isValid(self):
        return False


if __name__ == '__main__':
    pr1, pu1 = generate_keys()
    pr2, pu2 = generate_keys()
    pr3, pu3 = generate_keys()

    Tx1 = TX()
    Tx1.add_input(pu1, 1)
    Tx1.add_output(pu2, 1)
    Tx1.sign(pr1)

    if Tx1.isValid():
        print("Success! Tx is valid")

    savefile = open("tx.dat", "wb")
    pickle.dump(Tx1, savefile)
    savefile.close()

    loadfile = open("tx.dat", "rb")
    newTx = pickle.load(loadfile)

    if newTx.isValid():
        print("Sucess! Loaded tx is valid")
    loadfile.close()

    #Creating Blocks
    root = TxBlock()
    root.addTx(Tx1)


    Tx2 = TX()
    Tx2.add_input(pu1,1)
    Tx2.add_output(pu2,1)
    Tx2.sign(pr1)
    B1 = TxBlock(root)

    print(Tx2.isValid())

    savefile = open('tx2.dat','wb')
    pickle.dump()