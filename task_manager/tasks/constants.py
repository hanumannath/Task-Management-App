from enum import Enum

class TaskStatus(Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'


class TaskType(Enum):
    GENERAL = 'general'
    URGENT = 'urgent'
    OPTIONAL = 'optional'