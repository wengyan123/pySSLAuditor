import ssl
import socket
import logging


class SSLAuditor:
    _debug = False

    _socket_timeout = 10
    _sock = None

    _protocol = ssl.PROTOCOL_TLSv1
    _ssl_context = None
    _ssl_sock = None

    #
    # init params:
    # timeout
    # protocol version
    #
    def __init__(self, **kwargs):
        # set logger
        if 'debug' in kwargs and type(kwargs['debug']) == bool:
            self._debug = kwargs['debug']
        self.logger = self.__create_logger(debug=self._debug)

        # set socket timeout
        if 'timeout' in kwargs and type(kwargs['timeout']) == int:
            self._socket_timeout = kwargs['timeout']

        # set protocol version
        if 'protocol' in kwargs and type(kwargs['protocol']) == str:
            self._protocol = kwargs['protocol']


    def __create_logger(self, debug):
        if debug:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(name)s %(levelname)s %(message)s')
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s %(name)s %(levelname)s %(message)s')
        logger = logging.getLogger('RestClient')
        return logger

    def __decode_address(self, addr):
        if addr.find(':') == -1:
            _hostname = addr
            _port = 443
        else:
            _hostname, _port = addr.split(':')
        _addr = (_hostname, int(_port))
        return _addr


    def __create_socket(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.settimeout(self._socket_timeout)
        #_addr_tuple = self.__decode_address(addr)
        #self._sock.connect(_addr_tuple)


    def __init_SSLContext(self):
        self._ssl_context = ssl.SSLContext(protocol=self._protocol)
        #self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)



    def set_SSLContext(self):
        self._ssl_context.verify_mode = ssl.CERT_NONE
        self._ssl_check_hostname = False


    def __warp_SSLSocket(self):
        self._ssl_sock = self._ssl_context.wrap_socket(self._sock, server_side=False, do_handshake_on_connect=True)


    def ssl_handshake(self):
        self._ssl_sock.do_handshake()


    def ssl_connect(self, addr):
        _addr_tuple = self.__decode_address(addr)
        self._ssl_sock.connect(_addr_tuple)

    def ssl_setup(self, addr):
        self.__create_socket()
        self.__init_SSLContext()
        self.set_SSLContext()
        self.__warp_SSLSocket()
        #self.ssl_handshake()
        self.ssl_connect(addr)
        cert = self._ssl_sock.getpeercert()
        print(cert)


















