from backend.blockchain.block import Block, GENESIS_DATA

# Method for mining block and genesis block
def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block,data)
    # Insure block object is an instance of the block itself
    assert isinstance(block,Block)
    assert block.data == data
    assert block.last_hash == last_block.hash

def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis,Block)
    # every attirubte matches attribute in genesis block dictionary
    for key, value in GENESIS_DATA.items():
        getattr(genesis,key) == value 
    # Another way
    # assert genesis.timestamp == GENESIS_DATA['timestamp']
    # assert genesis.last_hash == GENESIS_DATA['last_hash']
    # assert genesis.hash == GENESIS_DATA['hash']
    # assert genesis.data == GENESIS_DATA['data']