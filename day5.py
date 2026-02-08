# import pdb

# x = [1,2,3,4, 5]

# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f = f * i
#     return f

# pdb.set_trace()
# print(fact(5))


import logging
logging.basicConfig(
    level = logging.WARNING,
    # format = "%(asctime)s %(levelname)s %(message)s",
    # filename='app.log',
    # filemode= "a"
)

logging.debug("Degub message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical Message")

#numpy pandas requests beautifulsoup4 matplotlib 
