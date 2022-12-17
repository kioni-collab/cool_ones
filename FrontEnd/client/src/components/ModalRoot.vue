<template>
<!-- Source used to make the popup: https://github.com/DJanoskova/Vue.js-Modal-context/blob/master/src/components/common/Modal.vue -->

  <Modal :isOpen="!!component" :title="title" @onClose="handleClose">
    <component :is="component" @onClose="handleClose" v-bind="props" />
  </Modal>
</template>

<script>
import { ModalBus } from '../eventBus'
import Modal from './Modal'
export default {
  data () {
    return {
      component: null,
      title: '',
      props: null
    }
  },
  created () {
    ModalBus.$on('open', ({ component, title = '', props = null }) => {
      this.component = component
      this.title = title
      this.props = props
    })
  },
  methods: {
    handleClose () {
      this.component = null
    }
  },
  components: { Modal },
}
</script>