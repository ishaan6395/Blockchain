import Signatures

class TX():

    input_addr = None
    output_addr = None
    sigs = None
    reqd = None

    def __init__(self):
        self.input_addr = []
        self.output_addr = []
        self.sigs = []
        self.reqd = []

    def add_input(self, sender, amount):
        self.input_addr.append((sender, amount))

    def add_output(self, receiver, amount):
        self.output_addr.append((receiver, amount))

    def add_reqs(self, addr):
        self.reqd.append(addr)

    def sign(self, private):
        message = self.__gather()
        newSig = Signatures.sign(message, private)
        self.sigs.append(newSig)

    def isValid(self):
        message = self.__gather()
        total_in = 0
        total_out = 0

        for addr, amount in self.input_addr:
            found = False
            for s in self.sigs:
                if Signatures.verify(message, s, addr):
                    found = True
            if not found:
               return False
            total_in+=amount

        for addr in self.reqd:
            found = False
            for s in self.sigs:
                if Signatures.verify(message, s, addr):
                    found = True
            if not found:
                return False
        for addr, amount in self.output_addr:
            if amount < 0:
                return False
            total_out = total_out + amount

        if total_in<total_out:
            return False
        return found

    def __gather(self):
        data = []
        data.append(self.input_addr)
        data.append(self.output_addr)
        data.append(self.reqd)
        return data

if __name__=='__main__':
    pr1, pu1 = Signatures.generate_keys()
    pr2, pu2 = Signatures.generate_keys()
    pr3, pu3 = Signatures.generate_keys()
    pr4, pu4 = Signatures.generate_keys()

    tx1 = TX()

    tx1.add_input(pu1, 1)
    tx1.add_output(pu2, 1)
    tx1.sign(pr1)


    tx2 = TX()

    tx2.add_input(pu1, 2)
    tx2.add_output(pu2, 1)
    tx2.add_output(pu3, 1)
    tx2.sign(pr1)




    tx3 = TX()
    tx3.add_input(pu3, 1.2)
    tx3.add_output(pu1, 1.1)
    tx3.add_reqs(pu4)
    tx3.sign(pr3)
    tx3.sign(pr4)


    tx4 = TX()
    tx4.add_input(pu1 , 1)
    tx4.add_output(pu2, 1)
    tx4.sign(pr2)

    tx5 = TX()
    tx5.add_input(pu1, 1)
    tx5.add_input(pu2, 1)
    tx5.add_output(pu3, 2)
    tx5.sign(pr2)

    tx6 = TX()
    tx6.add_input(pu1, 1)
    tx6.add_output(pu2, 1.2)
    tx6.sign(pr1)

    tx = [tx1, tx2, tx3, tx4, tx5, tx6]
    for t in tx:
        if t.isValid():
            print('Valid!!')
        else:
            print('Invalid!!')