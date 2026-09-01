"""
MESH — Bus — Barramento de Eventos
Regra combinada:
- Constituição = EVOLUTIVA
- Histórico (event_store) = IMUTÁVEL

O bus garante que todo evento seja registrado no histórico
imutável e distribuído para os agentes certos.
"""

from typing import Dict, Any, List, Callable
import uuid

class EventBus:
    def __init__(self, event_store):
        self.event_store = event_store
        self.subscribers: Dict[str, List[Callable]] = {}
        print("🚌 EventBus iniciado — histórico imutável conectado")

    def subscribe(self, event_type: str, handler: Callable):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)
        print(f"📡 Inscrito em: {event_type}")

    def publish(self, event_type: str, payload: Dict[str, Any]) -> str:
        trace_id = str(uuid.uuid4())[:8]
        event = {
            "trace_id": trace_id,
            "type": event_type,
            "payload": payload
        }

        # Registra no histórico IMUTÁVEL
        self.event_store.append(event)

        # Notifica inscritos
        if event_type in self.subscribers:
            for handler in self.subscribers[event_type]:
                try:
                    handler(event)
                except Exception as e:
                    print(f"⚠️ Erro no handler {event_type}: {e}")

        print(f"📤 Evento publicado: {event_type} | {trace_id}")
        return trace_id

    def get_history(self):
        return self.event_store.get_all()