class PoliceNode:
    def __init__(self, police_id, fine_amt):
        self.police_id = police_id
        self.fine_amt = fine_amt
        self.left = None
        self.right = None

    def initialize_hash(self):
        """
        def initializeHash (self):
        This function creates an empty hash table that points to null
        """

        main_hash = dict()

    def insert_hash(self, driver_hash, lic):
        """def insertHash (driverhash, lic):
        This function inserts the licence number lic to the hash table.
        If a driver’s license number is already present, only the number of violations need to be updated
        else a new entry has to be created
        """

    def print_violators(self, driver_hash):
        """ def printViolators (driverhash):
        This function prints the serious violators by looking through all
        hash table entries and printing the license numbers of the drivers who have more than 3
        violations onto the file violators.txt. The output should be in the format
        --------------Violators-------------
        <license no>, no of violations
        """

    def destroy_hash(self, driver_hash):
        """
        def destroyHash (driverhash): This function destroys all the entries inside the hash table. This
        is a clean-up code.
        """

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
