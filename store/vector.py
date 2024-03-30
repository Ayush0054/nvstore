import numpy as np

# arr =np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

class VectorStore:

 def __init__(self):
    self.vector_data={}
    self.vector_index={}
    
 def add_vector(self, index, value):
    self.vector_data[index] = value
    self._update_index(index,value)
    
 def get_vector(self,index):
    return self.vector_data.get(index)

 def _update_index(self,index,value):
    
    for existing_index , existing_value in self.vector_data.items():
        similarity = np.dot(value,existing_value)/(np.linalg.norm(value)*np.linalg.norm(existing_value))
        if existing_index not in self.vector_index:
            self.vector_index[existing_index] = {}
        self.vector_index[existing_index][index] = similarity
        
 def get_similarities(self, query_vector_value, num_results=1):
    result=[]
    for index,value in self.vector_data.items():
        similarity = np.dot(value,query_vector_value)/(np.linalg.norm(value)*np.linalg.norm(query_vector_value))
        result.append((index,similarity))
    result.sort(key=lambda x:x[1],reverse=True)
    return result[:num_results]
