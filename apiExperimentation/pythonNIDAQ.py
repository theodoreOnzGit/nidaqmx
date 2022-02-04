class nidaqmxWrappers:

    def __init__(self):

        print('welcome to nidaqmxWrapper class')

        self.buildNIDAQmxModule()


    def buildSystem(self):

        import nidaqmx.system
        system = nidaqmx.system.System.local()

        self.system = system


    def buildNIDAQmxModule(self):

        import nidaqmx
        self.nidaqmx = nidaqmx

        print(' ')
        print('NIDAQmx module imported, use self.nidaqmx to access it')
        print(' ')

    def printDevices(self):

        system = self.system

        for device in system.devices:

            print(device)


    def printDeviceName(self):

        system = self.system

        for device in system.devices:

            print(device)

            # uncomment the code below to see what kind of object
            # ai_physical_chans is:

            # print(device.ai_physical_chans)
            # print(device.ai_physical_chans[0].name)

            # here we are printing analog inputs (ai) phyiscal channels

            for physChannel in device.ai_physical_chans:

                print(physChannel.name)
                print(type(physChannel.name))

            # uncomment the code below to see what kind of object
            # ao_physical_chans is:
            # print(device.ao_physical_chans)

            for physChannel in device.ao_physical_chans:

                print(physChannel.name)
                print(type(physChannel.name))


    def returnTaskObj(self):

        nidaqmx = self.nidaqmx

        taskObj = nidaqmx.Task()

        return taskObj

        



class test:

    def __init__(self):

        print('welcome to the test class')


    def testPrintDevices(self):

        print(' ')

        import pythonNIDAQ
        from pythonNIDAQ import nidaqmxWrappers

        nidaqObj = nidaqmxWrappers()

        nidaqObj.buildSystem()
        nidaqObj.printDevices()

        print('test complete')

        print(' ')

    def testPrintDeviceName(self):

        print(' ')

        import pythonNIDAQ
        from pythonNIDAQ import nidaqmxWrappers

        nidaqObj = nidaqmxWrappers()

        nidaqObj.buildSystem()
        nidaqObj.printDeviceName()

        print('test complete')

        print(' ')

    def getNidaqObj(self):

        from importlib import reload

        import pythonNIDAQ
        reload(pythonNIDAQ)
        from pythonNIDAQ import nidaqmxWrappers

        nidaqObj = nidaqmxWrappers()

        return nidaqObj


    def testTask(self):

        nidaqObj = self.getNidaqObj()

        nidaqObj.buildSystem()

        taskObj = nidaqObj.returnTaskObj()

        print(type(taskObj))
        print(taskObj)

        taskObj.ai_channels.add_ai_voltage_chan('tempSensor1/ai7')
        taskObj.read()

        #taskObj.ai_channels.add_ai_thrmstr_chan_vex('tempSensor1/ai6')
        #taskObj.read()

        







class workspace:

    def __init__(self):

        print('initialising workspace')

        self.initialiseDefaults()


    def getTestObj(self):

        self.reloadClasses()
        self.testObj = self.test()

        return self.testObj

    def getNidaqmxWrappersObj(self):

        self.reloadClasses()
        self.nidaqmxWrappersObj = self.nidaqmxWrappers()

        return self.nidaqmxWrappersObj



    def initialiseDefaults(self):

        import pythonNIDAQ

        from pythonNIDAQ import nidaqmxWrappers
        from pythonNIDAQ import test

        self.nidaqmxWrappers = nidaqmxWrappers
        self.test = test

        from importlib import reload
        self.reload = reload

        print("workspace defaults initiated")

    def reloadClasses(self):

        reload = self.reload

        import pythonNIDAQ
        reload(pythonNIDAQ)


        from pythonNIDAQ import nidaqmxWrappers
        from pythonNIDAQ import test

        self.nidaqmxWrappers = nidaqmxWrappers
        self.test = test


def printHelp():

    print('hello, welcome to the pythonDAQmxWrapper module')

    print(' ')

    print('to load test modules use:')

    print(' ')

    print('import pythonNIDAQ')
    print('self = pythonNIDAQ.workspace()')

    print(' ')
    print('testObj = self.getTestObj()')

    print(' ')
    print('to load the nidaqmxWrappers object use:')

    print('nidaqmxWrapperObj = self.getNidaqmxWrappersObj()')


printHelp()


