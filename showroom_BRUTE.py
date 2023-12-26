class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.nextNode = None
        self.prevNode = None 


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0
        


class Car:
    def __init__(self, identification: int, name: str, brand: str, price: int, active: bool):
        self.identification = identification
        self.name = name
        self.price = price
        self.brand = brand
        self.active = active


db = LinkedList()


def init(cars: list[Car]):
    for car in cars: 
        add(car)
    return db


def add(car: Car):
    new_node = Node(car)
    if db.head == None:
        db.head = new_node
    else: 
        tmp = db.head
        if car.price < tmp.data.price:
            new_node.nextNode = db.head
            db.head.prevNode = new_node
            db.head = new_node
        else:
            while  tmp.nextNode and tmp.nextNode.data.price <= car.price:
                tmp = tmp.nextNode
            new_node.nextNode = tmp.nextNode 
            if tmp.nextNode:
                tmp.nextNode.prevNode = new_node
            tmp.nextNode = new_node
            new_node.prevNode = tmp   
             

        
 


def updateName(identification: int, name: str):
    tmp = db.head
    while tmp:
        if tmp.data.identification == identification:
            tmp.data.name = name
            break
        tmp = tmp.nextNode
        




def updateBrand(identification: int, brand: str):
    tmp = db.head
    while tmp:
        if tmp.data.identification == identification:
            tmp.data.brand = brand
            break
        tmp = tmp.nextNode


def activateCar( identification: int):
    tmp = db.head
    while tmp:
        if tmp.data.identification == identification:
            tmp.data.active = True
            break
        tmp = tmp.nextNode


def deactivateCar( identification: int):
    tmp = db.head
    while tmp:
        if tmp.data.identification == identification:
            tmp.data.active = False
            break
        tmp = tmp.nextNode


def getDatabaseHead():
    return db.head 


def getDatabase():
    return db


def calculateCarPrice():
    tmp = db.head
    db.count = 0
    while tmp:
        if tmp.data.active == True:
            db.count += tmp.data.price
        tmp = tmp.nextNode
    return db.count


def clean():
    db.head = None



