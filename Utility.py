import ConfigParser

class Utility:

    def __GetOptionValue(self, section, option):
        configParser = ConfigParser.SafeConfigParser()
        configParser.read('azure.cfg')
        
        optionValue = configParser.get(section, option)

        return optionValue

    
    def GetIoTHubHostName(self):
        iotHubHostName = self.__GetOptionValue('IoT', 'Host Name')
        
        return iotHubHostName


    def GetIoTHubSharedAccessKeyValue(self):
        iotHubSharedAccessKey = self.__GetOptionValue('IoT', 'Shared Access Key')

        return iotHubSharedAccessKey


    def GetEventHubNamespace(self):
        eventHubNamespace = self.__GetOptionValue('Event Hub', 'Namespace')

        return eventHubNamespace


    def GetEventHubSharedAccessKeyName(self):
        eventHubSharedAccessKeyName = self.__GetOptionValue('Event Hub', 'Shared Access Key Name')
        
        return eventHubSharedAccessKeyName
    

    def GetEventHubSharedAccessKeyValue(self):
        eventHubSharedAccessKeyValue = self.__GetOptionValue('Event Hub', 'Shared Access Key Value')

        return GetEventHubSharedAccessKeyValue   