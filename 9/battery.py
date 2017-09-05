class Battery():
    """To test the external instance as a attr"""
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
