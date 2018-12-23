
#
import datetime as date
#
import Block as blk


def create_genesis_block():
    return blk.Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return blk.Block(this_index, this_timestamp, this_data, this_hash)


if __name__ == "__main__":
    genesisBlock = create_genesis_block()

    blockchain = [genesisBlock]
    previous_block = blockchain[0]
    num_of_blocks_to_add = 20

    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))
