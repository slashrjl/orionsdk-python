import requests
from orionsdk import SwisClient
from datetime import datetime, timedelta


def main():
    hostname = 'localhost'
    username = 'admin'
    password = ''

    swis = SwisClient(hostname, username, password)
    results = swis.query('SELECT TOP 1 NodeID FROM Orion.Nodes')
    nodeId = results['results'][0]['NodeID']
    netObjectId = 'N:{}'.format(nodeId)
    now = datetime.utcnow()
    tomorrow = now + timedelta(days=1)
    swis.invoke('Orion.Nodes', 'Unmanage', netObjectId, now, tomorrow, False)


requests.packages.urllib3.disable_warnings()


if __name__ == '__main__':
    main()
