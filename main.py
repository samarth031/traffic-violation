class PoliceNode:
    def __init__(self, police_id, fine_amt):
        self.police_id = police_id
        self.fine_amt = fine_amt
        self.left = None
        self.right = None

    def initialize_hash(self):
        size = 30
        self.table = [[] for i in range(30)]

    def insert_hash(self, driver_hash, lic):
        assert driver_hash, tuple # driver_hash is a tuple in the format (lic, violations)
        def hash_map(key):
            return hash(key) % len(self.table) # hashing the key is lic has alphabets, hash(num) = num

        hash_index = hash_map(lic)
        key_present = False
        create_bucket = self.table[hash_index]
        for i, kv in enumerate(create_bucket):
            k, v = kv

            if lic == k:
                key_present = True
                break
        if key_present:
            print("This License Number is already present, updating only the violations")
            create_bucket[i].append(lic,driver_hash[1] + v) # This is assuming driver_hash is a tuple
        else:
            print("This License Number is not present, updating the key, val")
            create_bucket.append(driver_hash)


    def print_violators(self, driver_hash):
        assert driver_hash, tuple
        """
        --------------Violators-------------
        <license no>, no of violations
        """
        with open('Violators.txt', 'r') as f:
            for i, kv in enumerate(self.table):
                for k, v in kv:
                    if v > 3:
                        f.write("{}, {} \n".format(k, v))
        


    def destroy_hash(self, driver_hash):
        """
        def destroyHash (driverhash): This function destroys all the entries inside the hash table. This
        is a clean-up code.
        """
        self.table = [None]

    def insert_by_police_id(self):
        """
        def insertByPoliceId (policeRoot, policeId, amount):
        This function inserts an entry <policeId,
        amount> into the police tree ordered by police id. If the Police id is already found in the tree, then
        this function adds up to the existing amount to get the total amount collected by him. This function
        returns the updated tree.
        """

    def reorder_by_fine_amount(self):
        """
        def reorderByFineAmount (policeRoot):
        This function reorders the Binary Tree on the basis
        of total fine amount, instead of police id. This function removes the nodes from the original
        PoliceTree, and puts it in a new tree ordered by fine amount. Note that if the fine amount in node
        i is equal to the amount in node j, then the node i will be inserted to the left of the node j. This
        function returns the root node of the new tree.
        """

    def print_bonus_policeman(self, police_root):
        """
        def printBonusPolicemen (policeRoot):
        This function prints the list of police ids which have earned equal to or more than 90% of maximum total fine
        amount collected by an individual. The output is pushed to a file called bonus.txt. The output will be in the
        format
        -------------- Bonus -------------
        <license no>, no of violations
        """

    def destroy_police_tree(self, police_root):
        """
        def destroyPoliceTree (policeRoot): This function is a clean-up function that destroys all the
        nodes in the police tree
        """

    def print_police_tree(self, police_root):
        """
        def printPoliceTree (policeRoot):
        This function is meant for debugging purposes. This function
        prints the contents of the PoliceTree in-order.
        """
