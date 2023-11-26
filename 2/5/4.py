from queue import PriorityQueue


# class CCD(PriorityQueue):
#     def __init__(self, dict_inf):
#         super().__init__()
#         self.cat = dict_inf['cat']
#         self.union = dict_inf['union']
#         self.cargo = dict_inf['cargo']
#         self.id = dict_inf['id']

#     def __lt__(self, other):
#         if not isinstance(other, type(self)):
#             raise NotImplemented
        
#         if self.union and other.union:
#             if self.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209") and other.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209"):
#                 return self.id < other.id
#             elif self.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209"):
#                 return True
#             else:
#                 return False
#         elif self.union:
#             return True
#         else:
#             return False    
#         return False

#     def __repr__(self):
#         return f'{self.union}, {self.cat}, {self.id}, {self.cargo}'
    

# d1 = {"cat": "0210", "union": True, "cargo": {"stew", 2}, "id": 1}
# d2 = {"cat": "0208", "union": True, "cargo": {"liver", 1.78}, "id": 2}
# d3 = {"cat": "0208", "union": True, "cargo": {"liver", 56}, "id": 3}
# d4 = {"cat": "0209", "union": False, "cargo": {"pork fat", 100}, "id": 4}
# d5 = {"cat": "87", "union": False, "cargo": {"bombardier", 1}, "id": 5}


# products = [CCD(d1), CCD(d2), CCD(d3), CCD(d4), CCD(d5)]


# print(sorted(products))

# class CCD(PriorityQueue):
#     def __init__(self, dict_inf):
#         super().__init__()
#         self.cat = dict_inf['cat']
#         self.union = dict_inf['union']
#         self.cargo = dict_inf['cargo']
#         self.id = dict_inf['id']

#     def __lt__(self, other):
#         if not isinstance(other, type(self)):
#             raise NotImplemented
        
#         if self.union and other.union:
#             if self.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209") and other.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209"):
#                 return self.id > other.id
#             elif self.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209"):
#                 return False
#             else:
#                 return True
#         elif self.union:
#             return True
#         else:
#             return True    
#         return True

#     def __repr__(self):
#         return f'{self.union}, {self.cat}, {self.id}, {self.cargo}'


class CCD(PriorityQueue):
    def __init__(self, dict_inf):
        super().__init__()
        self.cat = dict_inf['cat']
        self.union = dict_inf['union']
        self.cargo = dict_inf['cargo']
        self.id = dict_inf['id']

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise NotImplemented
        cat_self = True
        cat_other = True

        if self.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209"):
            cat_self = True
        else:
            cat_self = False

        if other.cat in ("0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209"):
            cat_other = True
        else:
            cat_other = False

        return (self.union, cat_self, -self.id) > (other.union, cat_other, -other.id)

    def __repr__(self):
        return f'{self.union}, {self.cat}, {self.id}, {self.cargo}'
    

d1 = {"cat": "0210", "union": True, "cargo": {"stew", 2}, "id": 1}
d2 = {"cat": "0208", "union": True, "cargo": {"liver", 1.78}, "id": 2}
d3 = {"cat": "0208", "union": True, "cargo": {"liver", 56}, "id": 3}
d4 = {"cat": "0209", "union": False, "cargo": {"pork fat", 100}, "id": 4}
d5 = {"cat": "87", "union": False, "cargo": {"bombardier", 1}, "id": 5}


products = [CCD(d1), CCD(d2), CCD(d3), CCD(d4), CCD(d5)]


print(sorted(products))
