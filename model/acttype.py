class ActType:
    obj_list =[]

    def __init__(self, params):
        # Unique ID generated by the system.
        self.actv_code_type_id = int(params[0]) if params[0] else None
        # The maximum number of characters allowed for values of this Activity Code.
        self.actv_short_len = float(params[1]) if params[1] else None
        # Sequence number for sorting.
        self.seq_num = int(params[2]) if params[2] else None
        # Each Activity Code has a list of possible values, any of which can be assigned to an activity. Activity
        # Codes allow you to classify and categorize activities.
        self.actv_code_type = params[3].strip()
        # Identifies the project which owns this Activity Code (if this is a project-level Activity Code).
        self.proj_id = int(params[4]) if params[4] else None
        # EPS Id element that
        self.wbs_id = params[5].strip()
        self.actv_code_type_scope = params[6].strip()
        ActType.obj_list.append(self)

    def get_id(self):
        return self.actv_code_type_id

    @classmethod
    def find_by_id(cls, id):
        """ Function to search list of activity code type by an ID

        Args:
            id: Unique ID generated by the system.

        Returns: ActType that matches the ID

        """
        obj = list(filter(lambda x: x.actv_code_type_id == id, cls.obj_list))
        if obj:
            return obj[0]
        return obj

    def __repr__(self):
        return self.actv_code_type

