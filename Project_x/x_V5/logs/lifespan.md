Why am i separating it in first place?

because I want to improve the testability, prevent concurrency bugs.

So far i m using global for liefspan variables its a bad practice.

what do you replace with it?

passing state explicitly throught pure dependency injection, encapsulating them within classes or Modules with controlled access or 
using a state management pattern

what method u using?

passing a unified state object using dependency injection



code explanation:

```
@dataclass(frozen=True)
class ReadOnlyDB:
    DB_URL: str = field(Default="" )
```

So, before the db url was outside at module level not secured.

here what i did is used @dataclass from dataclasses
where frozen= True where "frozen" means an object cannot be modified

Likewise, creating a dataclass with frozen=True means its instances are frozen and cannot be changed.

but then again it is not the safest method better way is to just save it to .env so i m gonna do that

`os.getenv("DB_URL")`

then created a class with BaseModel from pydantic

```
class AppStateContext(BaseModel):
    model_config = ConfigDict(arbitary_types_allowed=True)
    
    lang_model: Any
    tools: list[Any]
    catched_tools: list[Any]
    agent_lookup: dict[str, Any]
    pool: Any #AsyncConnectionPool
    checkpointer: Any #AsyncPostgresSaver
    fast_agent = dict[str, Any]
    smart_agent = dict[str, Any]
```
why pydantic container?

because i wanna insure stricty type safety, prevent runtime key error and it also offer rich code autocomplete throughout workspace

`model_config = ConfigDict(arbitary_types_allowed=True)`
This wil allow pydantic to accept arbitary (random) types like LangGraph savers or connection pools, dict etc..

it instructs the validation engine to accept unconstrained, custom Python types for model fields instead of raising a RuntimeError during declaration.
These custom types are validated simply by checking if the assigned value is an instance of the declared type.

however later it can cause problem when dumping the model to JSON,
pydantic might not know how to serializer the arbitary object by default.
So later I may  When dumping the model to JSON, Pydantic might not know how to serialize the arbitrary object by default. You may need to use the `model_config = ConfigDict(json_encoders={...})` setting or custom `__pydantic_serializer__`.

# Creation of lifespan

```@asynccontextmanager
async def lifespan(app: FastAPI):```

where `@asynccontextmanager` is a decorator from `contextlib`
module that lets u define async context managers using generator functions, avoiding the need to write custom classes with
`__aenter__` and `__aexit__` methods.

why used here?
because it is ideal for handling async resources(eg db pools, network sockets or file I/O)


some changes made inside lifespan:

1. system prompt in differnt file `sys_prompt = ReadOnly()`

2. connetion url is .env safe `os.getenv("DB_URL")`
3.  language_model path to check if the language is english or not is not hardcoded anymore.

`lang_model= load_model(str(MODEL_PATH))`

```
#.../parent_folder/project_folder)
CURRENT_DIR = Path(__file__).resolve().parent

#Go up one more level to the parent folder (.../parent_folder)
MODEL_PATH = CURRENT_DIR.parent

#Navigate into the models folder
MODEL_PATH = MODEL_PATH / "models" / "lid.176.ftz"
```
Above is what you called absolute path method to safely access path without exposing.

```
state_container = AppStateContext(
        lang_model=lang_model,
        tools=tools,
        catched_tools=catched_tools,
        agent_lookup=agent_lookup,
        pool=pool,
        checkpionter=checkpointer,
    )
```
This is uh state_container basically instantiating the container making so
it can access the variables indepedently and type safe.

then `yield`

and access it safely via `Request` from `FastAPI`

```

def get_ctx(request: Request) -> AppStateContext:
    """Dependency provider to safely access app state."""
    return request.state.context
```




