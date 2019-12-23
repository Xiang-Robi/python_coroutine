# python_coroutine

## Advantages of Coroutine over Multithreading
*  NO CPU scheduler overhead => Faster
*  Each thread has its own stack (8MB in Linux) in RAM => Lighter
*  NO locking on shared data structures => Safer
*  Python GIL => Usually only ONE thread is allowed
