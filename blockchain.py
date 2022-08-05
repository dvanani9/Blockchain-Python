import hashlib

class neuralcoinblock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "anna sends 2 nc to mike"
t2 = "bob sends 4.3 nc to mike"
t3 = "mike sends 3.2 nc to bob"
t4 = "daniel sends 0.3 nc to anna"
t5 = "mike sends 1 nc to charlie"
t6 = "mike sends 5.4 nc to daniel"
 

initial_block = neuralcoinblock("initial string", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = neuralcoinblock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)


third_block = neuralcoinblock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)






