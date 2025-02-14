'''
You are given a root directory path containing multiple subdirectories and files. 
Each file contains a list of integers (one or more per line). 
Your task is to traverse the directory structure, 
extract all integers from the files, and return the top K largest numbers found across all files.
'''

import heapq
import os

class FileSystemProcessor:
    def __init__(self,root:str,k:int):
        self.root=root
        self.k=k
        self.min_heap=[]
    
    def extract_numbers_from_file(self, file_path):
        """Extracts integers from a given file."""
        numbers = []
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            print(f"Warning: {file_path} does not exist or is not a valid file.")
            return numbers  # Return an empty list
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    for num in line.split():  # Splitting by whitespace
                        if num.isdigit():
                            numbers.append(int(num))
        except IOError as e:
            print(f"Error reading {file_path}: {e}")
        
        return numbers
                
            
    
    def traverse_directory(self,path):
        for entry in os.listdir(path):
            full_path=os.path.join(path,entry)
            if os.path.isdir(full_path):
                self.traverse_directory(full_path)
            else:
                numbers=self.extract_numbers_from_file(full_path)
                for num in numbers:
                    heapq.heappush(self.min_heap,num)
                    if len(self.min_heap)>self.k:
                        heapq.heappop(self.min_heap)
                
                        
        
    
    
    def get_top_k(self):
        self.traverse_directory(self.root)
        return self.min_heap

class TestFileSystemProcessor:
    @staticmethod
    def test_get_top_k():
        import tempfile
        import shutil
        
        test_dir = tempfile.mkdtemp()
        try:
            os.mkdir(os.path.join(test_dir, "subdir1"))
            
            with open(os.path.join(test_dir, "file1.txt"), "w") as f:
                f.write("12\n825892\n92389\n")
            
            with open(os.path.join(test_dir, "subdir1", "file6.txt"), "w") as f:
                f.write("238483\n12\n17888\n4\n")
            
            processor = FileSystemProcessor(test_dir, 2)
            result = processor.get_top_k()
            print(result)
            print("Test case passed!")
        
        finally:
            shutil.rmtree(test_dir) 

TestFileSystemProcessor.test_get_top_k()
        