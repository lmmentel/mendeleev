import httpx
from pathlib import Path
import asyncio
import json


base_url = (
    "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/element/{atomic_number}/JSON/"
)
semaphore = asyncio.Semaphore(10)


def save_json(data, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


async def fetch_with_retries(client: httpx.AsyncClient, url: str, retries=3):
    for attempt in range(retries):
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if attempt < retries - 1:
                backoff = 2**attempt
                print(f"Retrying {url} in {backoff}s due to error: {e}")
                await asyncio.sleep(backoff)
            else:
                print(f"Failed to fetch {url} after {retries} attempts: {e}")
                return None


async def fetch_and_save(client: httpx.AsyncClient, atomic_number: int, dest_dir: Path):
    url = base_url.format(atomic_number=atomic_number)
    async with semaphore:
        try:
            data = await fetch_with_retries(client, url)
            out_path = dest_dir / f"{atomic_number}.json"
            save_json(data, out_path)
            print(f"Saved response_{atomic_number}.json")
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")


async def fetch_pubchem_data_async(atomic_numbers: list[int], dest_dir: Path):
    async with httpx.AsyncClient() as client:
        tasks = [
            fetch_and_save(client, atomic_number, dest_dir)
            for atomic_number in atomic_numbers
        ]
        await asyncio.gather(*tasks)


def fetch_pubchem_data_sync(atomic_numbers: list[int], dest_dir: Path):
    """Fetch data for all elements from PubChem and save as JSON files synchronously."""

    for atomic_number in atomic_numbers:
        url = base_url.format(atomic_number=atomic_number)
        out_path = dest_dir / f"{atomic_number}.json"
        try:
            data = httpx.get(url).json()
            save_json(data, out_path)
            print(f"Saved data for atomic number {atomic_number} to {out_path}")
        except Exception as e:
            print(f"Failed for {atomic_number}: {e}")


if __name__ == "__main__":
    atomic_numbers = list(range(1, 119))
    data_path = Path(__file__).parents[2] / "data"
    dest_dir = data_path / "pubchem"
    dest_dir.mkdir(parents=True, exist_ok=True)

    # asyncio.run(fetch_pubchem_data_async(atomic_numbers, dest_dir))
    fetch_pubchem_data_sync(atomic_numbers, dest_dir)
