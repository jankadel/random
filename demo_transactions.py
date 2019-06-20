from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()

print(my_blockchain.chain[1].transactions)

my_blockchain.chain[1].transactions = "fake_transactions"

my_blockchain.validate_chain()

print(my_blockchain.chain[1].transactions)
