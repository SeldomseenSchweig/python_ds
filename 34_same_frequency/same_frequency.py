def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # num1 = [ n for n in str(num1)]
    # num2 = [ n for n in str(num2)]
    s_num1 = sorted(str(num1))
    s_num2 = sorted(str(num2))
    return s_num1 ==s_num2