"""
MESH — Event Store — Memória de Eventos IMUTÁVEL
Regra combinada: Este arquivo é o que NÃO pode ser apagado nem alterado.
O histórico é fiel, auditável, append-only e hash-chained.
A Constituição é evolutiva, mas o PASSADO registrado aqui é imutável.
"""

from typing import List, Dict, Any
from datetime import datetime, timezone
import hashlib
import json

class EventStore:
    def __init__(self):
        self.events: List[Dict[str, Any]] = []

    def _hash_event(self, event: Dict[str, Any]) -> str:
        # Cria hash do evento para encadeamento
        data = json.dumps(event, sort_keys=True, default=str)
        return hashlib.sha256(data.encode()).hexdigest()

    def append(self, event: Dict[str, Any]):
        # Garante timestamp UTC
        event = event.copy()
        event["timestamp"] = datetime.now(timezone.utc).isoformat()
        
        # Encadeia com hash anterior para garantir imutabilidade
        if self.events:
            prev_hash = self.events[-1].get("event_hash", "")
            event["prev_hash"] = prev_hash
        
        event["event_hash"] = self._hash_event(event)
        self.events.append(event)
        print(f"📦 Evento imutável registrado: {event.get('trace_id', 'sem_trace')} | hash: {event['event_hash'][:8]}...")

    def get_all(self) -> List[Dict[str, Any]]:
        return self.events.copy()  # retorna cópia para não permitir alteração externa
