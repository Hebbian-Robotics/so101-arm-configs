"""Install an arm profile and calibration."""

import argparse
import json
import os
import re
import tomllib
from pathlib import Path


def install_file(path: Path, contents: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("xb") as output:
            output.write(contents)
    except FileExistsError:
        if path.read_bytes() != contents:
            raise SystemExit(
                f"Refusing to overwrite a different file: {path}"
            ) from None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("serial", help="USB controller serial number")
    parser.add_argument("--port", required=True, help="Serial port on this machine")
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory for the generated profile",
    )
    arguments = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", arguments.serial):
        parser.error("serial must contain only letters, digits, hyphens or underscores")
    repository = Path(__file__).resolve().parent
    arm = repository / "arms" / arguments.serial
    template = (arm / "profile.toml").read_text()
    if template.count('"__LOCAL_PORT__"') != 1:
        raise SystemExit("Invalid profile port placeholder")
    profile = template.replace('"__LOCAL_PORT__"', json.dumps(arguments.port))
    configuration = tomllib.loads(profile)
    calibration_id = f"so101_{arguments.serial}"
    if configuration["feetech"]["calibration_ids"]["follower"] != calibration_id:
        raise SystemExit("Profile calibration ID does not match serial")
    calibration = (arm / "calibration.json").read_bytes()
    json.loads(calibration)
    if os.environ.get("HF_LEROBOT_CALIBRATION"):
        calibration_root = Path(os.environ["HF_LEROBOT_CALIBRATION"]).expanduser()
    elif os.environ.get("HF_LEROBOT_HOME"):
        calibration_root = (
            Path(os.environ["HF_LEROBOT_HOME"]).expanduser() / "calibration"
        )
    else:
        cache = Path(os.environ.get("XDG_CACHE_HOME", "~/.cache")).expanduser()
        hf_home = Path(
            os.environ.get("HF_HOME", str(cache / "huggingface"))
        ).expanduser()
        calibration_root = hf_home / "lerobot" / "calibration"
    destinations = [
        (
            arguments.output_dir.expanduser() / f"so101-{arguments.serial}.toml",
            profile.encode(),
        ),
        (
            calibration_root / "robots" / "so_follower" / f"{calibration_id}.json",
            calibration,
        ),
    ]
    for path, contents in destinations:
        if path.exists() and path.read_bytes() != contents:
            raise SystemExit(f"Refusing to overwrite a different file: {path}")
    for path, contents in destinations:
        install_file(path, contents)
        print(f"Installed {path}")


if __name__ == "__main__":
    main()
