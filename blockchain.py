#python standard library 
#https://docs.python.org/3/library/index.html


#only mine block can add transaction to blockchain 
# add transaction add transaction to to open_transactions then miner choose transaction from open_transaction to add block to blockchain
import functools
import hashlib as hl
#import json
import collections
import hash_util
import json
import pickle
#from hash_util import hash_block,hash_string_256
MINING_REWARD=10
#we can set any value we want for proof 
# genesis_block={
#             "previous_hash":"",
#             "index":0,
#             "transactions":[],
#             "proof":100
#             }
# blockchain=[genesis_block]

blockchain=[]
open_transactions=[]
# in reality owner will be "aghadowpganvlkajgwqep"
owner="Sami"
#set start with owner 
participants={"Sami"}

#pickle is not good for security we can change anything in file and it will work but with json we have security so we use json
#we have to get the data we saved before
#AttributeError: 'str' object has no attribute 'append'
#we have to translate back to normal object we had not string  so we need to use json for making it to object
#json.loads for convert to object 
def load_data():

    # with open("blockchain.txt",mode="r") as f:
    #     file_content=f.readlines()
    #     #they have to be saved in global variables
    #     global blockchain
    #     global open_transactions
    #     # blockchain=file_content[0]
    #     # open_transactions=file_content[1]
    #     #important first line is with \n in the end so we have to remove it 
    #     #we have to convert each transactions of block in list becasuse we saved  as orderedDict to be sure that data can be got in a correct way 
    #     blockchain=json.loads(file_content[0][:-1])
    #     blockchain=[{
    #     "previous_hash":block["previous_hash"],
    #     "index":block["index"],
    #     "transactions":[collections.OrderedDict([("sender",tx["sender"]),("recipient",tx["recipient"]),("amount",tx["amount"])]) for tx in block["transactions"]],
    #     "proof":block["proof"]
    #     } for block in blockchain]
    #     # updated_blockchain=[]
    #     # for block in blockchain:
    #     #     updated_block={
    #     #     "previous_hash":block["previous_hash"],
    #     #     "index":block["index"],
    #     #     "transactions":[collections.OrderedDict([("sender",tx["sender"]),("recipient",tx["recipient"]),("amount",tx["amount"])]) for tx in block["transactions"]],
    #     #     "proof":block["proof"]
    #     #     }
    #     #     updated_blockchain.append(updated_block)
    #     # blockchain=updated_blockchain
    #     #for open_transactions we have to do the same with orderedDict
    #     open_transactions=json.loads(file_content[1])
    #     open_transactions=[collections.OrderedDict([("sender",tx["sender"]),("recipient",tx["recipient"]),("amount",tx["amount"])]) for tx in open_transactions]
    #unpickle data 
    #mode should be rb for reading binary data 
    #we won't have problem in transactions because it will be in orderedDict with pickle
    # with open("blockchain.p",mode="rb") as f:
    #     file_content=pickle.loads(f.read())
    #     #print(file_content)
    #     #they have to be saved in global variables
    #     global blockchain
    #     global open_transactions
        
    #     blockchain=file_content["chain"]
    #     open_transactions=file_content["ot"]
    #back to json
    global blockchain
    global open_transactions
    try:
        with open("blockchain.txt",mode="r") as f:
            file_content=f.readlines()
            #they have to be saved in global variables
            # global blockchain
            # global open_transactions
            # blockchain=file_content[0]
            # open_transactions=file_content[1]
            #important first line is with \n in the end so we have to remove it 
            #we have to convert each transactions of block in list becasuse we saved  as orderedDict to be sure that data can be got in a correct way 
            blockchain=json.loads(file_content[0][:-1])
            #print("start",blockchain)
            blockchain=[{
            "previous_hash":block["previous_hash"],
            "index":block["index"],
            "transactions":[collections.OrderedDict([("sender",tx["sender"]),("recipient",tx["recipient"]),("amount",tx["amount"])]) for tx in block["transactions"]],
            "proof":block["proof"]
            } for block in blockchain]
            #print("final",blockchain)
            # updated_blockchain=[]
            # for block in blockchain:
            #     updated_block={
            #     "previous_hash":block["previous_hash"],
            #     "index":block["index"],
            #     "transactions":[collections.OrderedDict([("sender",tx["sender"]),("recipient",tx["recipient"]),("amount",tx["amount"])]) for tx in block["transactions"]],
            #     "proof":block["proof"]
            #     }
            #     updated_blockchain.append(updated_block)
            # blockchain=updated_blockchain
            #for open_transactions we have to do the same with orderedDict
            open_transactions=json.loads(file_content[1])
            open_transactions=[collections.OrderedDict([("sender",tx["sender"]),("recipient",tx["recipient"]),("amount",tx["amount"])]) for tx in open_transactions]

    except IOError:
        #print("file not found") 
        genesis_block={
            "previous_hash":"",
            "index":0,
            "transactions":[],
            "proof":100
            }
        blockchain=[genesis_block]
        open_transactions=[] 
    # except ValueError:
    #     print("value error")
    # except:
    #     print("other errors")
    finally:
        print("clean up")


load_data()


#method to save blockchain and open transactions to a file
#we have to call it when we have new transactions or mine data 
#TypeError: write() argument must be str, not list
#noraml str won't work we need to use json for making it string because we want to convert it back 
#we have to use json.dumps to convert to string
def save_data():
    # with open("blockchain.txt",mode="w") as f:
    #     f.write(blockchain)
    #     f.write("\n")
    #     f.write(open_transactions)
    # with open("blockchain.txt",mode="w") as f:
    #     # f.write(str(blockchain))
    #     # f.write("\n")
    #     # f.write(str(open_transactions))
    #     f.write(json.dumps(blockchain))
    #     f.write("\n")
    #     f.write(json.dumps(open_transactions))
    #pickle for saving in binary data 
    #we have to change mode to wb
    #we have to change file name to blockchain.p
    #we don't have "\n" for binary data 
    #so we have to create one object and pass blockchain and open_transactions as one object
    #we create new dictionary for all of the data 
    # with open("blockchain.p",mode="wb") as f:
    #     save_data={
    #     "chain":blockchain,
    #     "ot":open_transactions
    # }
    #     f.write(pickle.dumps(save_data))
    try:
        with open("blockchain.txt",mode="w") as f:
            # f.write(str(blockchain))
            # f.write("\n")
            # f.write(str(open_transactions))
            f.write(json.dumps(blockchain))
            f.write("\n")
            f.write(json.dumps(open_transactions))
    except IOError:
        print("saving failed")



#### so important
#in hash_block
#when we make things to string and pass them to sh256 we pass dictionary (block)
#and block is unordered thing (what if we pass in unordered way )
#and transaction of each transactions too and it's unorderd 
#so we have to make them to tuple and some how change them to be in order
#for block we pass sort_keys=True as second argument to json.dumps in hash_block
# for transactions we use collections and call orderedDict in add_transaction or reward_transaction
#orderDict takes a list of tuples as key value 






# def hash_block(block):
#     # hashed_block="-".join([str(value) for key,value in block.items()])
#     # return hashed_block
#     # return hashlib.sha256(json.dumps(block).encode()).hexdigest()
#     return hl.sha256(json.dumps(block).encode()).hexdigest()

# def hash_block(block):
#     # hashed_block="-".join([str(value) for key,value in block.items()])
#     # return hashed_block
#     # return hashlib.sha256(json.dumps(block).encode()).hexdigest()
#     return hl.sha256(json.dumps(block,sort_keys=True).encode()).hexdigest()




def valid_proof(transactions,last_hash,proof):
    #encode for making them utf-8 characters 
    #if we want to use sha256 we need string part which is encode too so first convert to string then use encode 
    #and finally call hexdigest() with it 
    guess=(str(transactions)+str(last_hash)+str(proof)).encode()
    # guess_hash=hl.sha256(guess).hexdigest()
    guess_hash=hash_util.hash_string_256(guess)
    print("guess_hash",guess_hash)
    return guess_hash[0:2]=="00"

def proof_of_work():
    last_block=blockchain[-1]
    # last_hash=hash_block(last_block)
    last_hash=hash_util.hash_block(last_block)
    proof=0
    while not valid_proof(open_transactions,last_hash,proof):
        proof+=1
    return proof

# how much the participant sent , received
#when we need nested one we have to use [] inside [] check tx_sender
#tx_sender=[[transaction["amount"] for transaction in block["transactions"] if transaction["sender"]==participant] for block in blockchain]
#[block["transactions"] for block in blockchain] give us array of all transactions in each block 
# we need nested [] again for for getting iterate all transactions  so block["transactions"] will be what we want to loop through it but we want amount part 
#[[transaction["amount"] for transaction in block["transactions"]] for block in blockchain] 
# as it's sender what we want we have if part and as we know all conditions will come after what we want to loop through it transaction["sender"]==participant] add it after  block["transactions"] (the thing we want to loop)
#tx_sender=[[transaction["amount"] for transaction in block["transactions"] if transaction["sender"]==participant for block in blockchain]
def get_balance(participant):
    tx_sender=[[transaction["amount"] for transaction in block["transactions"] if transaction["sender"]==participant] for block in blockchain]
    #we checked that each transaction should be in blance but maybe we have three transactions each of them is valid but combination of them is not 
    # so we have to check open_transactions for sender too 
    open_tx_sender=[tx["amount"] for tx in open_transactions if tx["sender"]==participant]
    print("open_tx_sender",open_tx_sender)
    # we have to add open_tx_sender to tx_sender
    tx_sender.append(open_tx_sender)
    tx_recipient=[[transaction["amount"] for transaction in block["transactions"] if transaction["recipient"]==participant] for block in blockchain]
    #first is a function which recieves last and current value tx_sum,tx_amt (sum last , amt current)
    #: the operation we have to do with arguments  :tx_sum+tx_amt[0]
    #second is the list tx_sender
    #third is the initial value 0
    # amount_sent=functools.reduce(lambda tx_sum,tx_amt:tx_sum+tx_amt[0],tx_sender,0)
    #if len of tx_amt is greater than 0 do what is infront of lambda else do the thing in front of else 
    # amount_sent=functools.reduce(lambda tx_sum,tx_amt:tx_sum+tx_amt[0] if len(tx_amt)>0 else 0,tx_sender,0)
    # amount_received=functools.reduce(lambda tx_sum,tx_amt:tx_sum+tx_amt[0] if len(tx_amt)>0 else 0,tx_recipient,0)
    #sum() will get a list and sum all of the elements in it 
    #we have to add tx_sum every time we received nothing or sent nothing 
    #it always have to pass tx_sum+ something (it can be tx_amt or sum of it when we have more than 0 value in list or it can be 0 when it's our first )
    # so important tx_sum comes from the sum of previous data you have to know that it's different than the sum we define as first 0 after tx_sender (...,tx_sender,0)
    # if len(tx_amt)>0 else 0 if we just put it 0 we said that all of the previous sum is always 0 which is not corrent 
    print("tx_sender before amount",tx_sender)
    amount_sent=functools.reduce(lambda tx_sum,tx_amt:tx_sum+sum(tx_amt) if len(tx_amt)>0 else tx_sum+0,tx_sender,0)
    #print("sent",amount_sent)
    amount_received=functools.reduce(lambda tx_sum,tx_amt:tx_sum+sum(tx_amt) if len(tx_amt)>0 else tx_sum+0,tx_recipient,0)
    # amount_sent=0
    #amount_received=0
    print("tx_sender after amount",tx_sender)
    # for tx in tx_sender:
    #     print("tx",tx)
    #     if len(tx)>0:
    #         #print("tx[0]",tx[0])
    #         for index,value in enumerate(tx):
    #             print("value",value)
    #             amount_sent+=value
    #         # amount_sent+=tx[0]
    # for tx in tx_recipient:
    #     #print("tx",tx)
    #     if len(tx)>0:
    #         amount_received+=tx[0]
    print("send",amount_sent)
    print("recieved",amount_received)
    return amount_received-amount_sent


def get_user_choice():
    user_choice=input("your choice: ")
    return user_choice


def get_last_blockchain_value():
    """ returns the last value 
    of our blockchain
    """
    if len(blockchain)<1:
        return None
    return blockchain[-1]

def get_transaction_value():
    tx_recipent=input("Enter the recipient of the transaction: ")
    tx_amount=float(input("Your transaction amount please: "))
    #we can use dictionary too but we use tuple here 
    # return (tx_recipent,tx_amount)
    return tx_recipent,tx_amount

def verify_transaction(transaction):
    sender_balance=get_balance(transaction["sender"])
    # if sender_balance>=transaction["amount"]:
    #     return True
    # else:
    #     return False
    return sender_balance>=transaction["amount"]

#optional stuff always comes after unoptional things
def add_transaction(recipient,sender=owner,amount=1.0):
    # transaction={
    #     "sender":sender,
    #     "recipient":recipient,
    #     "amount":amount 
    # }
    transaction=collections.OrderedDict([("sender",sender),("recipient",recipient),("amount",amount)])
    # if not verify_transaction(transaction):
    #     open_transactions.append(transaction)
    #     participants.add(sender)
    #     participants.add(recipient)
    #     return True
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False

# def add_transaction(transaction_amount,last_transaction):
#     if last_transaction==None:
#         last_transaction=[1]
#     blockchain.append([last_transaction,transaction_amount])

#we take open_transactions and add it to the block and mine a new block with all of transactions in open_transaction
#we have to create block
def mine_block():
    #block 1- hashed value of last block , 2- index which is len of blockchain(optional) ,3- list of transactions as data(open transactions)
    #for first block we don't have any last block so we create genesis block which is like block (check top of the file)
    last_block=blockchain[-1]
    # hashed_block=""
    # for key,value in last_block.items():
    #     hashed_block=hashed_block+ str(value)
    # hashed_block=str([value for key,value in last_block.items()])
    #note we can only join strings with together so all values should be string 
    # hashed_block="-".join([str(value) for key,value in last_block.items()])
    hashed_block=hash_util.hash_block(last_block)
    #print("hashedBlock",hashed_block)
    proof=proof_of_work()
    #reward for miner
    # reward_transaction={
    #     "sender":"MINING",
    #     "recipient":owner,
    #     "amount":MINING_REWARD
    # }
    reward_transaction=collections.OrderedDict([("sender","MINING"),("recipient",owner),("amount",MINING_REWARD)])
    copied_transactions=open_transactions[:]
    copied_transactions.append(reward_transaction)
    block={
        "previous_hash":hashed_block,
        "index":len(blockchain),
        "transactions":copied_transactions,
        "proof":proof
        }
    blockchain.append(block)
    save_data()
    #it won't work because it will be only vocal so we return True to empty open_transactions
    #open_transactions=[]
    return True

def print_blockchain_elements():
    for block in blockchain:
            print("outputting block")
            print(block)
    else:
        print("-"*20)
#first value of the block with the entire last block 
# def verify_chain():
#     is_valid=True
#     for index,block in enumerate(blockchain):
#         if index==0:
#             continue
#         if blockchain[index-1]==block[0]:
#             is_valid=True
#         else:
#             is_valid=False
#             break
#     return is_valid
# def verify_chain():
#     is_valid=True
#     print("entered to get verified")
#     for index,block in enumerate(blockchain):
#         if index==0:
#             continue
#         elif hash_block(blockchain[index-1])==block["previous_hash"]:
#             is_valid=True
#             print("valid")
#         else:
#             is_valid=False
#             print("invalid")
#             break
#     return is_valid

def verify_chain():
    print("entered to get verified")
    for index,block in enumerate(blockchain):
        if index==0:
            continue
        elif hash_util.hash_block(blockchain[index-1])!=block["previous_hash"]:
            #print("invalid")
            return False
        #we have reward and we don't want to validate that one so we have to remove reward from transactions for validation
        elif not valid_proof(block["transactions"][:-1],block["previous_hash"],block["proof"]):
            print("proof of work is invalid")
            return False
    return True

def verify_transactions():
    return all(verify_transaction(tx) for tx in open_transactions)



#add_value(get_transaction_value())



# while True:
#     print("please choose")
#     print("1: add a new transaction")
#     print("2: output blockchain")
#     print("h: manipulate blockchain")
#     print("q: quit")
#     user_choice=get_user_choice()
#     if user_choice=="1":
#         add_transaction(get_transaction_value(),get_last_blockchain_value())
#     elif user_choice=="2":
#         print_blockchain_elements()
#     elif user_choice=="h" or "H":
#         if len(blockchain)>=2:
#             blockchain[0]=[2]
#     elif user_choice=="q" or user_choice=="Q":
#         #continue
#         break
#     else:
#         print("input is invalid")
#     if not verify_chain():
#             print("invalid blockchain")
#             break
#     print("choice registered")


waiting_for_input=True
while waiting_for_input:
    print("please choose")
    print("1: add a new transaction")
    print("2: Mine a new block")
    print("3: output blockchain")
    print("4: output participants")
    print("5: check transactions validity")
    print("h: manipulate blockchain")
    print("q: quit")
    user_choice=get_user_choice()
    if user_choice=="1":
        #getting the values of tuple
        #unpacking tuple 
        recipient,amount=get_transaction_value()
        if add_transaction(recipient,amount=amount):
            print("open_transaction",open_transactions)
        else:
            print("transaction failed")
    elif user_choice=="2":
        # mine_block()
        if mine_block():
            open_transactions=[]
            #we need to save data here because we changed open_transactions 
            save_data()
    elif user_choice=="3":
        print_blockchain_elements()
    elif user_choice=="4":
        print(participants)
    elif user_choice=="5":
        if verify_transactions():
            print("all transactions are valid")
        else:
            print("there are invalid transactions")
    elif user_choice=="h" or user_choice=="H":
        if len(blockchain)>=1:
            blockchain[0]={
            "previous_hash":"",
            "index":0,
            "transactions":[{"sender":"Chris","recipient":"Jake","amount":10}]
            }
    elif user_choice=="q" or user_choice=="Q":
        #continue
        waiting_for_input=False
    else:
        print("input is invalid")
    if not verify_chain():
            print("invalid blockchain")
            break
    # print(get_balance("Sami"))
    print("Balance of {}:{:6.2f}".format("Sami",get_balance("Sami")))
    print("choice registered")


print("blockchain",blockchain)
