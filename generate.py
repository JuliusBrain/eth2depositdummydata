from eth2spec.phase0.spec import DepositData
from eth2spec.utils.ssz.ssz_typing import List
from eth2spec.utils.ssz.ssz_impl import hash_tree_root
import secrets
import sys


def deposit_input(pubkey, witdrawal_credentials, signature, amount):
    """
    pubkey: bytes[48]
    withdrawal_credentials: bytes[32]
    signature: bytes[96]
    deposit_data_root: bytes[32]
    """
    return (
        "0x"+pubkey.hex(),
        "0x"+witdrawal_credentials.hex(),
        "0x"+signature.hex(),
        hash_tree_root(
            DepositData(
                pubkey=pubkey,
                withdrawal_credentials=witdrawal_credentials,
                amount=amount,
                signature=signature,
            ),
        )
    )


def generateInputs(eth_amount):
    eth = eth_amount * 1e18
    gwei = 1e9
    deposit_amount = eth // gwei
    sample_withdrawal_credentials = secrets.token_bytes(32)
    sample_pubkey = secrets.token_bytes(48)
    sample_valid_signature = secrets.token_bytes(96)
    inputs = deposit_input(
        sample_pubkey, sample_withdrawal_credentials, sample_valid_signature, int(deposit_amount)
        )
    return {
        'pubkeys': inputs[0], 'withdrawal_credentials': inputs[1], 'signatures': inputs[2], 'deposit_data_roots': inputs[3]
    }


def main(argv):
    if len(argv) == 2:
        generatedInputs = generateInputs(int(argv[1]))
        print(generatedInputs)
    else:
        print("Usage:\n First parameter: ETH deposit (in N * eth nominals) amount per one transaction")


if __name__ == "__main__":
    main(sys.argv[1])
