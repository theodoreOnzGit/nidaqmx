class nidaqmxWrappers:

    def __init__(self):

        print('welcome to nidaqmxWrapper class')


    def buildSystem(self):

        import nidaqmx.system
        system = nidaqmx.system.System.local()

        self.system = system

    def printDevices(self):

        system = self.system

        for device in system.devices:

            print(device)


    def printDeviceName(self):

        system = self.system

        for device in system.devices:

            print(device)
            print(device.ai_physical_chans[0].name)

            print(device.ai_physical_chans)



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
    print('from pythonNIDAQ import workspace')
    print('self = workspace()')

    print(' ')
    print('testObj = self.getTestObj()')

    print(' ')
    print('to load the nidaqmxWrappers object use:')

    print('nidaqmxWrapperObj = self.getNidaqmxWrappersObj()')


printHelp()


