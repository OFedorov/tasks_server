#!/bin/python
from time import sleep

import workers
from server import Server


def execution_delay(function, delay=0):
    '''Sets the execution delay of the function to simulate the execution time'''
    def wrapper(data):
        sleep(delay)
        return function(data)
    return wrapper


if __name__ == "__main__":
    from argparse import ArgumentParser

    argp = ArgumentParser()
    # argp.add_argument("--server_config", "-s", type=str, action="store", dest="server", default=None,
    #                  required=False)
    argp.add_argument("--host", type=str, action="store", dest="host", required=True)
    argp.add_argument("--port", type=int, action="store", dest="port", required=True)
    argp.add_argument("--receiving_buffer_size", "-r", type=int, action="store", dest="buffer_size", default=1024,
                      required=False)
    argp.add_argument("--connection_limit", "-l", type=int, action="store", dest="connection_limit", default=1000,
                      required=False)
    argp.add_argument("--timeout", "-t", type=int, action="store", dest="timeout", default=None, required=False)
    args = argp.parse_args()

    test_server = Server(host=args.host,
                         port=args.port,
                         connection_limit=args.connection_limit,
                         receiving_buffer_size=args.buffer_size,
                         timeout=args.timeout)

    # set workers
    test_server.set_worker(task_type="echo", worker=workers.echo)
    test_server.set_worker(task_type="revers", worker=execution_delay(workers.revers, 2))
    test_server.set_worker(task_type="permutation", worker=execution_delay(workers.permutation, 5))
    test_server.set_worker(task_type="too_long_echo", worker=execution_delay(workers.echo, 20))

    # run server
    test_server.run()