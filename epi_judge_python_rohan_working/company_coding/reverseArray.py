def reverseWords(s):
        """
        Do not return anything, modify s in-place instead.
        """
        window_start = 0
        for window_end in range(len(s)):
            if (s[window_end] == ' ') or (window_end == len(s) - 1):
                if window_end != len(s) - 1:
                    i, j = window_start, window_end - 1
                else:
                    i , j = window_start, window_end
                while i < j:
                    s[i], s[j] = s[j] , s[i]

                    i += 1
                    j -= 1
                if window_end != len(s) - 1:
                    window_start = window_end + 1
        i, j = 0 , len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


        return s

print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
