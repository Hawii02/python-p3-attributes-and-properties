#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "Itc",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Guido", job="Marketing"):
        # self.name = None
        # self.job = None
        self.name = name
        self.job = job 
        # if job in APPROVED_JOBS else print("Job must be in list of approved jobs.")

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_name(self):
        return self._name

        
    def set_job(self, job):
        
        # return "Hereeee"
        # print(job)
        if job.title() in APPROVED_JOBS: 
            self._job = job
            # return "Persons job added"
        else:
            # self._job =None
            print ("Job must be in list of approved jobs.")

    def get_job(self):
        return self._job

    
    name = property(get_name, set_name)
    job = property(get_job, set_job)

# Wafula = Person("", "")
person2 = Person(job="Benevolent dictator for life")
    


