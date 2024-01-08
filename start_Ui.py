import sys
sys.path.append('.')

from ui import run_osr2,run_app,date_dict_init,short_key_func
import multiprocessing


if  __name__ == '__main__':
    manager = multiprocessing.Manager()
    date_dict = manager.dict()
    date_dict_init(date_dict)

    
    p0 = multiprocessing.Process(target=run_app,args=(date_dict,))
    p1 = multiprocessing.Process(target=short_key_func,args=(date_dict,))
    p2 = multiprocessing.Process(target=run_osr2,args=(date_dict,))
    p0.start()
    p1.start()
    p2.start()
    p0.join()
    p1.join()
    p2.join()

