print(ord("a"))

def decode_message(msg):
    try:
        # create a num variable to store and return the decoded message
        num = ''
        # loop through the message
        for i in msg:
            # convert each character to its ascii value
            num += str(ord(i))
        # return the decoded message
        return num
    # if there is an error, return the original message
    
    except:
        return msg
    


decode_message('hi')