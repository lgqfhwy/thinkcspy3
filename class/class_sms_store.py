class SMS_store:
    """ Similar to an inbox or outbox on a cellphone."""
    def __init__(self):
        self.message_list = []
        pass

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ 
            Makes new SMS tuple, inserts it after other messages
            in the store. When creating this message, its has_been_viewed
            status is set False.
        """
        self.message_list.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        """
            Return the number of SMS message in my_box
        """
        return len(self.message_list)

    def get_unread_indexes(self):
        """
            Return list of indexes of all not-yet-viewed SMS message
        """
        not_read = []
        for (i, v) in enumerate(self.message_list):
            if v[0] == False:
                not_read.append(i)
        return not_read

    def get_message(self, i):
        """
            Return (from_number, time_arrived, text_of_SMS) for message[i]
            Also change its state to "has been viewed".
            If there is no message at position i, return None
        """
        if len(self.message_list) <= i:
            return None
        from_number = self.message_list[i][1]
        time_arrived = self.message_list[i][2]
        text_of_SMS = self.message_list[i][3]
        if self.message_list[i][0] == False:
            self.message_list[i] = (True, from_number, time_arrived, text_of_SMS)
        return (from_number, time_arrived, text_of_SMS)

    def delete(self, i):
        """ Delete the message at index i """
        if len(self.message_list) <= i:
            return None
        self.message_list.pop(i)
        return

    def clear(self):
        """ Delete all messages from inbox."""
        self.message_list = []
        return
























