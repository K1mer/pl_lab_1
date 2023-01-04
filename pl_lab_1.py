import re;
import sys;
from os.path import basename;
from datetime import datetime, timedelta;
from urllib.parse import urlparse;
from urllib.request import urlopen;

CONST_REGEX_URL = "https?:\/\/(?:www\.)?([-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b)*(\/[\/\d\w\.-]*)*(?:[\?])*(.+)*";

def doDownload( url, fileName ):
    print( 'Sending Http request...' );
    response = urlopen( url );
    print( 'Success!' );

    newFile = open( fileName, 'wb' );
    
    bytesSumm = 0;
    curTime = datetime.now();
    for test_bytes in response.__iter__():
        newFile.write( test_bytes );
        bytesSumm += len( test_bytes );

        if datetime.now() > curTime + timedelta( seconds = 1 ):
            print( f'{ bytesSumm } bytes received.' )
            curTime = datetime.now();

    print( f'File "{ fileName }" ({ bytesSumm } bytes) was successfully downloaded!' )

def main( argv ):
    downloadUrl = argv[ 1 ] if len( argv ) > 1 else '';
    
    if re.search( CONST_REGEX_URL, downloadUrl ):
        fileName = basename( urlparse( downloadUrl ).path );

        if fileName:
            doDownload( downloadUrl, fileName );
        else:
            print( 'Unable to get file name.' );
    else:
        print( 'URL was not found.' );

if __name__ == '__main__':
    main( sys.argv );