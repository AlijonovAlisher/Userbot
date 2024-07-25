from environs import Env
env = Env()
env.read_env()


api_id = env.int("api_id")
api_hash = env.str("api_hash")
phone_number =  env.str("phone_number")