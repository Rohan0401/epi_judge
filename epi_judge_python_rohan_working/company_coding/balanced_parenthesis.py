def isValid(s):

    # Initate a stack
    stack = []

    mapping = {")" : "(", "]" : "[", "}" : "{"}

    for ele in s:

        if ele in mapping :
            top_element = stack.pop() if stack else "#"

            if mapping[ele] != top_element:
                return False

        else:
            stack.append(ele)

    return not stack

print(isValid("{[()]}"))




