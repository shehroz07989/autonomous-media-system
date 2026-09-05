class Run:
    ALLOWED_TRANSITIONS = {
        "PENDING": {"RUNNING"},
        "RUNNING": {"SUCCESS", "FAILED"},
        "SUCCESS": set(),
        "FAILED": set()
        }

    def __init__(self, run_id, query):
        self.run_id = run_id
        self.query = query
        self.status = "PENDING"
        self.current_stage = None
    def change_status(self, new_status):
        allowed_statuses = self.ALLOWED_TRANSITIONS[self.status]
        if not isinstance(new_status,str):
            raise TypeError("INVALID_TYPE")
        if new_status in allowed_statuses:
            self.status = new_status
        else:
            raise ValueError(f"ILLEGAL_TRANSITION ({self.status}) ---> {new_status}")
        



def discover():
    return "discover_success"
def research():
    return "research_success_"

def plan():
    return "plan_success"

def generate():
    return "generate_success"

def verify():
    return "verify_success"

def publish():
    return "publish_success"


STAGE_HANDLERS = {
        "DISCOVER": discover,
        "RESEARCH": research,
        "PLAN": plan,
        "GENERATE": generate,
        "VERIFY": verify,
        "PUBLISH": publish
    }
def stage_execute(stage_name):
    
    stage_to_execute = STAGE_HANDLERS.get(stage_name)
    if stage_to_execute is None:
        raise ValueError("Unknown_Stage_Name")
    return stage_to_execute()


run = Run("123", "make a video")
stage = run.current_stage = "BANANA"
result = stage_execute(stage)
print (result)