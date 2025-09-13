import sys. # sys module is interacted with the Python interpreter.
# it will connect property, method, function to the interpreter.

def error_msg_detail(error_msg, error_details: sys):
    print(error_details)
    _, _, exc_tb = error_details.exc_info()
    # here we are using the 'exc_info()' method of sys module to get the exception information.
    # it returns a tuple of three values: (type, value, traceback).
    # we are only interested in the third value which is the traceback object.
    # so we are using '_' to ignore the first two values.
    # it is used to capture file name and line number where the exception occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename
    # overall it gives file information where the exception occurred.
    # 'exc_tb' is the traceback object.
    # here we are using the 'tb_frame' attribute of traceback object to get the frame object.
    # then we are using the 'f_code' attribute of frame object to get the code object.
    # finally, we are using the 'co_filename' attribute of code object to
    # get the file name where the exception occurred.
    error_msg = "Error occurred in script: [{0}] line number: [{1}] error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error_msg)
    )
    return error_msg





class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg) # here super() fn is used to access properties of parent class i.e 'Exception' class.
        self.error_msg = error_msg_detail(error_msg, error_detail=error_detail)
        # here we are calling the fn 'error_msg_detail' which take two parameters.
        # first is 'error_msg' which is passed while creating the object of this class.
        # second is 'error_msg_details' which is the sys module.
        # this fn will return the formatted error message which we are storing in 'self.error_msg' attribute.

    def __str__(self):
        return self.error_msg
        # this method is used to return the string representation of the object.
        # here we are returning the formatted error message stored in 'self.error_msg' attribute.