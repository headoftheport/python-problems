"""unique email Ids"""
class Solution:
    """solution"""
    def num_unique_email(self, emails) -> int:
        """
        string search
        time complexity : O(sum(len of emailIds in string))
        space complexity: O(unique email Ids) 
        """
        mails = set()
        
        
        for email in emails:
            string = ''
            index = 0
            ignore = False
            while index < len(email) and email[index] != '@':
                if ignore or email[index] == '.':
                    index = index + 1
                    continue
                if email[index] == '+':
                    ignore = True
                else:
                    string += email[index]
                index = index + 1
                
            
            mails.add(string + email[index:len(email)])
            
        return len(mails)