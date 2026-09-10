# 4-guards/proposal_gate.py - PROPOSER não ganha authority
def check_proposal(proposal: dict) -> bool:
    if proposal.get("authority") != "none":
        raise PermissionError("Learning never grants authority")
    # bloqueia tentativa de escrever em 1-fundacao-alicerce
    target = proposal.get("target", "")
    if "1-fundacao-alicerce" in target:
        raise PermissionError("Fundacao imutavel - escrita negada")
    return True
