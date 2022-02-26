class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
            
        window_length = len(s)        
        window_count = 1   # Count of windows
        
        while window_length > 1:
                    
            if window_length % 2 == 0:
                # Means the string is an even length string
                half_len = window_length / 2
                
                # This loop is for each individual window of the current window size
                for window_id in range (0, window_count):
                    curr_start = window_id
                    curr_stop = window_length + window_id - 1
                    
                    curr_size = 0
                    curr_palindrome = True
                    
                    while curr_size < half_len and curr_palindrome == True:
                        if s[curr_start] != s[curr_stop]:
                            curr_palindrome = False
                        curr_size += 1
                        curr_start += 1
                        curr_stop -= 1
                    
                    if curr_palindrome == True:
                        stop = window_length + window_id
                        return s[window_id:stop]
            
            else:
                # Means the string is an odd length string
                for window_id in range (0, window_count):
                    curr_start = window_id
                    curr_stop = window_length + window_id - 1
                    
                    curr_palindrome = True
                    
                    while (curr_start != curr_stop) and curr_palindrome == True:
                        if s[curr_start] != s[curr_stop]:
                            curr_palindrome = False
                        curr_start += 1
                        curr_stop -= 1
                    
                    if curr_palindrome == True:
                        stop = window_length + window_id
                        return s[window_id:stop]
            
            window_count += 1
            window_length -= 1
        
        return s[0]

if __name__ == "__main__":
    def test1(str):
        sol = Solution()
        retstr = sol.longestPalindrome(str)
        print (str, retstr) 
        print (len(str), len(retstr))      

    # Include any test code here
    test1("abcdaaabcdeffedcbaabcdaaa")
    test1("baaa")
    test1("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")