from SSLAuditor import SSLAuditor
import unittest
import subprocess


class SSLTestCase(unittest.TestCase):

    def test_ssl_version(self):
        sslauditor = SSLAuditor()
        sslauditor.ssl_setup('127.0.0.1:12443')

    def test_ciphersuite(self):
        pass

    def test_get_peer_cert(self):
        pass

    def test_verify_server_cert(self):
        pass

    def test_mutual_authen(self):
        pass

    def test_hostname(self):
        pass


if __name__ == '__main__':
    testSuite = unittest.TestLoader().loadTestsFromTestCase(SSLTestCase)
    unittest.TextTestRunner(verbosity=2).run(testSuite)
