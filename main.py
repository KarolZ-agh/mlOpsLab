import argparse

from dotenv import load_dotenv

from settings import Settings


def export_envs(environment: str = "dev") -> None:
    load_dotenv(dotenv_path=environment, verbose=True, override=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    settings = Settings(_env_file=".env." + args.environment)

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
