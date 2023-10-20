def bracket_match(text):
    '''
    input: string
    output: int
    outliers: none
    edge cases: none

    1. iterate over the string
    2. keep count of opening and closing of par.
       - plus for opening
       - minus for closing
       - if the total is zero and ) is the next char -> add to a l_par_needed count
       - if the total count at the end is > 0 at the end of iteration -> set to r_par_needed
       return the sum of l_par_needed and r_par_needed

       l_par_needed = 0
       r_par_needed = 0 -> 1
       ex: ())(
           i
       l_par_needed = 0
       r_par_needed = 1 -> 0
       ex: ())(
            i
       l_par_needed = 0 -> 1
       r_par_needed = 0
       ex: ())(
             i
       l_par_needed = 1
       r_par_needed = 0 -> 1
       ex: ())(
              i
       l_par_needed = 1
       r_par_needed = 1
       total parentheses needed to correctly match
       time complexity: 0(n)
       space complexity: 0(1)
    '''
    l_par_needed = 0
    r_par_needed = 0
    for t in text:
        if t == '(':
            r_par_needed += 1
        if t == ')':
            if r_par_needed == 0:
                l_par_needed += 1
            else:
                r_par_needed -= 1
    return l_par_needed + r_par_needed
