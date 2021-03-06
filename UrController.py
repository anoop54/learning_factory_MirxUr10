#Learning Factory 2018.
#Authors: Anoop Gadhrri & Simran Nijjar

import socket
import time
import struct
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

class MyUR:
    HOST = "10.0.2.64" #Remote Host for UR5 Robot
    PORT = 30003        #Available Ports (30001, 30002, 30003)
    HOST2 = "10.0.8.50" #Remote Host2 for UR5 Robot
    
    #UR5 Robot Joint Data in Radians
    UR_Home =     ("movej([-3.1258847, -1.5767304, 1.5449655, 1.58825, 1.57 , 0.04468043], a=0.5236, v=1.0)" + "\n")
    UR_TakePic =  ("movej([-0.6937, -2.04, 1.753, 0.06, 2.51, -0.178], a=0.5236, v=1.0)" + "\n")

    #Bin_Position
    #Waypoint1 =   ("movej([-1.5304792, -2.16281201, 1.537286, 0.61348323, 1.576905, -0.005061455], a=1.0472, v=1.39626)" + "\n")
    Waypoint2 =   ("movej([-1.5304792, -2.16281201, 1.537286, 0.61348323, 1.576905, -0.005061455], a=0.5236, v=1.39626)" + "\n")
    Waypoint3 =   ("movej([-3.11872884, -2.136283, 1.5313519, 0.5899213, 1.6474163,-0.03560472], a=0.5236, v=1.39626)" + "\n")
    Waypoint4 =   ("movej([-3.11611085, -2.33106175, 2.31151406, 0.04572763, 1.6509069, -0.01012291], a=0.5236, v=1.39626)" + "\n")
    Waypoint5 =   ("movej([-3.84757834, -1.1629129, 1.425934, -0.23055799, -0.71942472, -0.05131268], a=0.5236, v=1.39626)" + "\n")

    Waypoint6 =   ("movel([-3.84356408, -1.085595, 1.5414748, -0.42359141, -0.7145378, -0.05096361], a=0.10, v=0.25)" + "\n")
    Waypoint7 =   ("movel([-3.84356408, -1.0691887, 1.5594517, -0.45814893, -0.71436326, -0.05096361], a=0.02, v=0.25)" + "\n")
    Waypoint8 =   ("movel([-3.81668601, -1.0878637, 1.5887732, -0.4677482, -0.6876597, -0.05253441], a=0.02, v=0.25)" + "\n")
    Waypoint9 =   ("movel([-3.81668601, -1.041962, 1.6269959, -0.55204764, -0.68731066, -0.05218534], a=0.10, v=0.25)" + "\n")
    Waypoint10 =  ("movel([-3.95561422, -0.92746796, 1.4325663, -0.47664942, -0.82623887, -0.04607669], a=0.10, v=0.25)" + "\n")

    Waypoint11 =  ("movej([-3.81267175, -1.415462, 1.736603, -1.88496, -1.5803956, 0.87720248], a=0.5236, v=1.0)" + "\n")
    Waypoint12 =  ("movej([-3.84775287, -1.8940313, 1.74812178, -1.4182546, -1.5807447, 0.84002697], a=0.5236, v=1.0)" + "\n")

    #Drop_Off_Picture
    Waypoint13 =  ("movej([-3.117158, -1.98862815, 1.83364291, 0.1666789, 0.07906342, 0.003316126], a=0.5236, v=1.0)" + "\n")
    Waypoint14 =  ("movej([-1.93888627, -2.05687052, 1.86278991, 0.22916173, 1.2281882, -0.03385939], a=0.5236, v=1.0)" + "\n")
    Waypoint15 =  ("movel([-2.17834544, -0.9843657, 2.53491621, -1.5861552, 1.01229, -0.0137881], a=0.1, v=0.75)" + "\n")
    Waypoint16 =  ("movel([-2.17729824, -1.7025687, 2.40733264, -0.74193947, 1.0114183, -0.01082104], a=0.1, v=0.75)" + "\n")

    #Camera Trigger Commands
    Trigger_True = "set_digital_out(0,True)"+"\n"
    Trigger_False = "set_digital_out(0,False)"+"\n"

    count = 0
    home_status = 0
    program_run = 0


    def getCurrentPos(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((self.HOST, self.PORT))
            time.sleep(1.00)
            print("")
            packet_1 = s.recv(4)
            packet_2 = s.recv(8)
            packet_3 = s.recv(48)
            packet_4 = s.recv(48)
            packet_5 = s.recv(48)
            packet_6 = s.recv(48)
            packet_7 = s.recv(48) 
            packet_8 = s.recv(48)
            packet_9 = s.recv(48)
            packet_10 = s.recv(48)
            packet_11 = s.recv(48)

            packet_12 = s.recv(8)
            x = struct.unpack('!d', packet_12)[0]
            print ("X = ", x * 1000)

            packet_13 = s.recv(8)
            y = struct.unpack('!d', packet_13)[0]
            print ("Y = ", y * 1000)

            packet_14 = s.recv(8)
            z = struct.unpack('!d', packet_14)[0]
            print ("Z = ", z * 1000)

            packet_15 = s.recv(8)
            Rx = struct.unpack('!d', packet_15)[0]
            print ("Rx = ", Rx)

            packet_16 = s.recv(8)
            Ry = struct.unpack('!d', packet_16)[0]
            print ("Ry = ", Ry)

            packet_17 = s.recv(8)
            Rz = struct.unpack('!d', packet_17)[0]
            print ("Rz = ", Rz)

            home_status = 1
            program_run = 0
            s.close()
            return(x,y,z,Rx,Ry,Rz)
        
        except socket.error as socketerror:
            print("Error: ", socketerror)
            print("Unable To Connect To UR")
            
        
    def MoveDelta(self,x,y,z,s=1,rx=0,ry=0,rz=0):
        xo,yo,zo,rxo,ryo,rzo = self.getCurrentPos()
        x = xo*1000+x
        y = yo*1000+y
        z = zo*1000+z
        rx = rxo+rx
        ry = ryo+ry
        rz = rzo+rz    
        UR_Move = "movel(p["+str(x/1000.0)+ ", "+ str(y/1000.0) + ", "+ str(z/1000) + ", "+ str(rx)+", "+str(ry)+", "+str(rz)+"], a="+str(s)+", v=1)" + "\n"
        print(UR_Move)
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST, self.PORT))
            s.send(Ur_Move.encode())
            data= s.recv(1024)
            s.close()
            
        except socket.error as socketerror:
            print("Error: ", socketerror)
            print("Unable To Connect To UR")

        print("UR_Action: Move Complete")

        
    def MoveAbs(self,x,y,z,rx=0,ry=0,rz=0):
        UR_Move = "movej(p["+str(x/1000.0)+ ", "+ str(y/1000.0) + ", "+ str(z/1000) + ", "+ str(rx)+", "+str(ry)+", "+str(rz)+"], a=1.0, v=1)" + "\n"
        print(UR_Move)
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST, self.PORT))
            s.send(Ur_Move.encode())
            data= s.recv(1024)
            s.close()
            
        except socket.error as socketerror:
            print("Error: ", socketerror)
            print("Unable To Connect To UR")

        print("UR_Action: Move Complete")

        
    def MoveCommand(self, command):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST, self.PORT))
            s.send(command.encode())
            data= s.recv(1024)
            s.close()
            
        except socket.error as socketerror:
            print("Error: ", socketerror)
            print("Unable To Connect To UR")         
        print("UR_Action: Move Complete")


    def Home(self):
        self.MoveCommand(self.UR_Home)


    def TakePic(self):
        self.MoveCommand(self.UR_TakePic)
        time.sleep(5)


    def PicTrigger(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST,self.PORT))
        s.send(self.Trigger_True.encode())
        time.sleep(1.5)
        s.send(self.Trigger_False.encode())
        data= s.recv(1024)
        s.close()
        print("UR_Action: Picture Triggered")


    def UR2_Start(self):
        while 1:
            try:
                client = ModbusClient('10.0.8.50', port=502)

                while 1:
                    try:
                        client.connect()
                        break
                    except:
                        print("NO SERVER CONNECTION")
                        time.sleep(1)

                print("CONNECTED TO SERVER")
                print(client.connect())
                client.write_register(1, 64, unit=1)  # 2^7
                print("wrote to bit 6")
                time.sleep(1)
                client.write_register(3, 64, unit=1)
                break
            except Exception as e:
                print(e)


    def Bin_Position(self):
        self.MoveCommand(self.Waypoint2)
        time.sleep(3)
        self.MoveCommand(self.Waypoint3)
        time.sleep(3.5)
        self.MoveCommand(self.Waypoint4)
        time.sleep(2.5)
        self.MoveCommand(self.Waypoint5)
        time.sleep(4)
        self.MoveCommand(self.Waypoint6)
        time.sleep(1.75)
        self.MoveCommand(self.Waypoint7)
        time.sleep(1.75)
        self.MoveCommand(self.Waypoint8)
        time.sleep(2.25)
        self.MoveCommand(self.Waypoint9)
        time.sleep(1.25)
        self.MoveCommand(self.Waypoint10)
        time.sleep(2)
        self.MoveCommand(self.Waypoint11)
        time.sleep(3.5)
        self.MoveCommand(self.Waypoint12)
        time.sleep(2)
        self.MoveCommand(self.UR_Home)
        time.sleep(5)


    def Drop_Off_Picture(self):
        self.MoveCommand(self.Waypoint13)
        time.sleep(3.5)
        self.MoveCommand(self.Waypoint15)
        time.sleep(5)

        
    def Drop_Off(self):
        self.MoveCommand(self.Waypoint13)
        time.sleep(3.75)
        self.MoveCommand(self.Waypoint12)
        time.sleep(3.5)
        self.MoveCommand(self.Waypoint11)
        time.sleep(2)
        self.MoveCommand(self.Waypoint10)
        time.sleep(4)
        self.MoveCommand(self.Waypoint9)
        time.sleep(2)
        self.MoveCommand(self.Waypoint8)
        time.sleep(2.75)
        self.MoveCommand(self.Waypoint5)
        time.sleep(1.25)
        self.MoveCommand(self.Waypoint13)
        time.sleep(2.75)
        self.MoveCommand(self.Waypoint16)
        time.sleep(4)

        
